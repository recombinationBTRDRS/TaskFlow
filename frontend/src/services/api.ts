import axios from "axios";
import type {
  Task,
  CreateTaskRequest,
  UpdateTaskRequest,
  Category,
  Tag,
} from "@/types/task";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || "http://localhost:8000/api",
  timeout: 10000,
});

// Request interceptor
api.interceptors.request.use(
  (config) => {
    // Add auth token if needed
    return config;
  },
  (error) => Promise.reject(error)
);

// Response interceptor
api.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error("API Error:", error.response?.data || error.message);
    return Promise.reject(error);
  }
);

export const taskApi = {
  getTasks: (params?: Record<string, any>) =>
    api.get<Task[]>("/tasks", { params }),

  getTask: (id: number) => api.get<Task>(`/tasks/${id}`),

  createTask: (data: CreateTaskRequest) => api.post<Task>("/tasks", data),

  updateTask: (id: number, data: Partial<UpdateTaskRequest>) =>
    api.put<Task>(`/tasks/${id}`, data),

  deleteTask: (id: number) => api.delete(`/tasks/${id}`),

  startTask: (id: number) => api.post<Task>(`/tasks/${id}/start`),

  stopTask: (id: number) => api.post<Task>(`/tasks/${id}/stop`),
};

export const categoryApi = {
  getCategories: () => api.get<Category[]>("/categories"),

  createCategory: (data: Omit<Category, "id" | "created_at">) =>
    api.post<Category>("/categories", data),

  updateCategory: (id: number, data: Partial<Category>) =>
    api.put<Category>(`/categories/${id}`, data),

  deleteCategory: (id: number) => api.delete(`/categories/${id}`),
};

export const tagApi = {
  getTags: () => api.get<Tag[]>("/tags"),

  createTag: (data: Omit<Tag, "id" | "created_at">) =>
    api.post<Tag>("/tags", data),

  updateTag: (id: number, data: Partial<Tag>) =>
    api.put<Tag>(`/tags/${id}`, data),

  deleteTag: (id: number) => api.delete(`/tags/${id}`),
};

export default api;
