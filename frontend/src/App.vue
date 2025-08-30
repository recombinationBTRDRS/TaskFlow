<template>
  <div id="app" class="min-h-screen bg-gray-50 dark:bg-gray-900">
    <RouterView />
  </div>
</template>

<script setup lang="ts">
import { RouterView } from "vue-router";
import { onMounted } from "vue";
import { useWebSocketStore } from "@/stores/websocket";

const wsStore = useWebSocketStore();

onMounted(() => {
  // Initialize WebSocket connection
  wsStore.connect();
});
</script>

<style>
#app {
  font-family: "Inter", Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
