import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:5000/api',
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
