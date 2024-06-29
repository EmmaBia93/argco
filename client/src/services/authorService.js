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
  getAuthors() {
    return apiClient.get('/authors');
  },
  getAuthor(id) {
    return apiClient.get(`/authors/${id}`);
  }
};
