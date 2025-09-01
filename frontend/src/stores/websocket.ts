// src/stores/websocket.ts
import { defineStore } from "pinia";

export const useWebSocketStore = defineStore("websocket", {
  state: () => ({
    connected: false,
    socket: null as WebSocket | null,
  }),
  actions: {
    connect() {
      this.socket = new WebSocket("ws://localhost:8000/ws");
      this.socket.onopen = () => {
        this.connected = true;
        console.log("WebSocket connected");
      };
      this.socket.onclose = () => {
        this.connected = false;
        console.log("WebSocket disconnected");
      };
    },
  },
});
