import { defineStore } from "pinia";
import { ref, computed } from "vue";
import type { Task, CreateTaskRequest, UpdateTaskRequest } from "@/types/task";
import { taskApi } from "@/services/api";

export const useTasksStore = defineStore("tasks", () => {
  // State
  const tasks = ref<Task[]>([]);
  const loading = ref(false);
  const error = ref<string | null>(null);

  // Getters
  const todayTasks = computed(() => {
    const today = new Date().toISOString().split("T")[0];
    return tasks.value
      .filter((task) => task.start_time.split("T")[0] === today)
      .sort(
        (a, b) =>
          new Date(a.start_time).getTime() - new Date(b.start_time).getTime()
      );
  });

  const activeTasks = computed(() =>
    tasks.value.filter((task) => task.start_time && !task.end_time)
  );

  // Actions
  async function fetchTasks(filters?: {
    date?: string;
    category_id?: number;
    tag_id?: number;
  }) {
    loading.value = true;
    error.value = null;

    try {
      const response = await taskApi.getTasks(filters);
      tasks.value = response.data;
    } catch (err) {
      error.value = "Failed to fetch tasks";
      console.error(err);
    } finally {
      loading.value = false;
    }
  }

  async function createTask(taskData: CreateTaskRequest) {
    try {
      const response = await taskApi.createTask(taskData);
      tasks.value.push(response.data);
      return response.data;
    } catch (err) {
      error.value = "Failed to create task";
      throw err;
    }
  }

  async function updateTask(id: number, taskData: Partial<UpdateTaskRequest>) {
    try {
      const response = await taskApi.updateTask(id, taskData);
      const index = tasks.value.findIndex((t) => t.id === id);
      if (index !== -1) {
        tasks.value[index] = response.data;
      }
      return response.data;
    } catch (err) {
      error.value = "Failed to update task";
      throw err;
    }
  }

  async function deleteTask(id: number) {
    try {
      await taskApi.deleteTask(id);
      tasks.value = tasks.value.filter((t) => t.id !== id);
    } catch (err) {
      error.value = "Failed to delete task";
      throw err;
    }
  }

  async function startTask(id: number) {
    return updateTask(id, { start_time: new Date().toISOString() });
  }

  async function stopTask(id: number) {
    return updateTask(id, { end_time: new Date().toISOString() });
  }

  // WebSocket handlers
  function handleTaskUpdate(task: Task) {
    const index = tasks.value.findIndex((t) => t.id === task.id);
    if (index !== -1) {
      tasks.value[index] = task;
    } else {
      tasks.value.push(task);
    }
  }

  function handleTaskDelete(taskId: number) {
    tasks.value = tasks.value.filter((t) => t.id !== taskId);
  }

  return {
    // State
    tasks,
    loading,
    error,
    // Getters
    todayTasks,
    activeTasks,
    // Actions
    fetchTasks,
    createTask,
    updateTask,
    deleteTask,
    startTask,
    stopTask,
    // WebSocket handlers
    handleTaskUpdate,
    handleTaskDelete,
  };
});
