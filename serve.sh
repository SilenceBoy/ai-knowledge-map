#!/usr/bin/env bash
# serve.sh — 启动本地静态服务器
# 用法：./serve.sh [端口]，默认使用 8765

set -euo pipefail

PORT="${1:-8765}"

# 检查端口是否被占用
PID=$(lsof -ti tcp:"$PORT" 2>/dev/null || true)

if [[ -n "$PID" ]]; then
  echo "⚠️  端口 $PORT 已被占用 (PID: $PID)，正在 kill..."
  kill -9 $PID
  # 等待端口释放
  sleep 0.5
  echo "✅  已释放端口 $PORT"
fi

LOG_FILE="/tmp/serve-$PORT.log"

# 后台启动静态服务器
nohup python3 -m http.server "$PORT" >"$LOG_FILE" 2>&1 &
SERVER_PID=$!

echo "🚀  静态服务器已在后台启动 → http://localhost:$PORT"
echo "     PID: $SERVER_PID"
echo "     日志: $LOG_FILE"
echo "     停止服务: kill $SERVER_PID  (或 ./serve.sh $PORT 重启)"
