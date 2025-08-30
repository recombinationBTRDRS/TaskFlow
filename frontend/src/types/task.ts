export interface Task {
  id: number;
  title: string;
  description?: string;
  category_id: number;
  subcategory_id?: number;
  start_time: string;
  end_time?: string;
  duration?: number;
  created_at: string;
  updated_at: string;
  tags: Tag[];
  category: Category;
  subcategory?: Subcategory;
}

export interface CreateTaskRequest {
  title: string;
  description?: string;
  category_id: number;
  subcategory_id?: number;
  start_time?: string;
  end_time?: string;
  duration?: number;
  tag_ids?: number[];
}

export interface UpdateTaskRequest extends Partial<CreateTaskRequest> {
  id: number;
}

export interface Category {
  id: number;
  name: string;
  color: string;
  description?: string;
  created_at: string;
}

export interface Subcategory {
  id: number;
  name: string;
  category_id: number;
  created_at: string;
}

export interface Tag {
  id: number;
  name: string;
  color: string;
  created_at: string;
}
