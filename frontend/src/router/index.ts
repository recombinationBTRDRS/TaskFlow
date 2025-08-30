import { createRouter, createWebHistory } from "vue-router";
import Dashboard from "@/views/Dashboard.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name: "dashboard",
      component: Dashboard,
    },
    {
      path: "/tasks",
      name: "tasks",
      component: () => import("@/views/Tasks.vue"),
    },
    {
      path: "/categories",
      name: "categories",
      component: () => import("@/views/Categories.vue"),
    },
    {
      path: "/analytics",
      name: "analytics",
      component: () => import("@/views/Analytics.vue"),
    },
  ],
});

export default router;
