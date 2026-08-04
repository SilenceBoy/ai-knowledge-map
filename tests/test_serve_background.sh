#!/usr/bin/env bash

set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEST_DIR="$(mktemp -d "${TMPDIR:-/tmp}/ai-knowledge-map-serve.XXXXXX")"
PORT="$(python3 - <<'PY'
import socket

with socket.socket() as sock:
    sock.bind(("127.0.0.1", 0))
    print(sock.getsockname()[1])
PY
)"
SCRIPT_PID=""

cleanup() {
  local server_pids

  if [[ -n "$SCRIPT_PID" ]] && kill -0 "$SCRIPT_PID" 2>/dev/null; then
    kill "$SCRIPT_PID" 2>/dev/null || true
  fi

  server_pids="$(lsof -ti tcp:"$PORT" 2>/dev/null || true)"
  if [[ -n "$server_pids" ]]; then
    kill $server_pids 2>/dev/null || true
  fi

  rm -rf "$TEST_DIR"
}
trap cleanup EXIT

cp "$PROJECT_ROOT/serve.sh" "$TEST_DIR/serve.sh"
chmod +x "$TEST_DIR/serve.sh"
printf 'background server test\n' > "$TEST_DIR/index.html"

(
  cd "$TEST_DIR"
  exec ./serve.sh "$PORT"
) > "$TEST_DIR/command.out" 2>&1 &
SCRIPT_PID=$!

for _ in {1..50}; do
  RUNNING_JOBS="$(jobs -pr)"
  if [[ "$RUNNING_JOBS" != "$SCRIPT_PID" ]]; then
    break
  fi
  sleep 0.1
done

if [[ "$RUNNING_JOBS" == "$SCRIPT_PID" ]]; then
  echo "FAIL: serve.sh 仍在前台运行" >&2
  exit 1
fi

wait "$SCRIPT_PID"

response="$(curl --fail --silent --show-error "http://127.0.0.1:$PORT/")"
if [[ "$response" != *"background server test"* ]]; then
  echo "FAIL: serve.sh 退出后，静态服务器不可访问" >&2
  exit 1
fi

echo "PASS: serve.sh 已退出，静态服务器仍在后台运行"
