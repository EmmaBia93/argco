import axios from 'axios';
import { API_URL } from '../consts';

const apiClient = axios.create({
  baseURL: `${API_URL}`,
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json'
  }
});

export default {
  getCategories() {
    return apiClient.get('/categories');
  },
  getCategory(id) {
    return apiClient.get(`/categories/${id}`);
  }
};
