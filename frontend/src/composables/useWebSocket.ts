import { ref, onMounted, onUnmounted } from "vue";
import { useTasksStore } from "@/stores/tasks";

export function useWebSocket() {
  const ws = ref<WebSocket | null>(null);
  const connected = ref(false);
  const reconnectAttempts = ref(0);
  const maxReconnectAttempts = 5;

  const tasksStore = useTasksStore();

  const connect = () => {
    const wsUrl = import.meta.env.VITE_WS_URL || "ws://localhost:8000/ws";
    ws.value = new WebSocket(wsUrl);

    ws.value.onopen = () => {
      console.log("WebSocket connected");
      connected.value = true;
      reconnectAttempts.value = 0;
    };

    ws.value.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data);
        handleMessage(data);
      } catch (error) {
        console.error("Failed to parse WebSocket message:", error);
      }
    };

    ws.value.onclose = () => {
      console.log("WebSocket disconnected");
      connected.value = false;

      // Auto-reconnect
      if (reconnectAttempts.value < maxReconnectAttempts) {
        reconnectAttempts.value++;
        setTimeout(() => {
          connect();
        }, 1000 * reconnectAttempts.value);
      }
    };

    ws.value.onerror = (error) => {
      console.error("WebSocket error:", error);
    };
  };

  const handleMessage = (data: any) => {
    switch (data.type) {
      case "task_updated":
      case "task_created":
        tasksStore.handleTaskUpdate(data.task);
        break;
      case "task_deleted":
        tasksStore.handleTaskDelete(data.task_id);
        break;
      default:
        console.log("Unknown WebSocket message type:", data.type);
    }
  };

  const disconnect = () => {
    if (ws.value) {
      ws.value.close();
      ws.value = null;
      connected.value = false;
    }
  };

  onMounted(() => {
    connect();
  });

  onUnmounted(() => {
    disconnect();
  });

  return {
    connected,
    connect,
    disconnect,
  };
}
