import categoryService from "../services/categoryService";

export default {
  namespaced: true,
  state: {
    categories: [],
  },
  mutations: {
    SET_CATEGORIES(state, categories) {
      state.categories = categories;
    },
  },
  actions: {
    fetchCategories({ commit }) {
      categoryService
        .getCategories()
        .then((response) => {
          commit("SET_CATEGORIES", response.data);
        })
        .catch((error) => {
          console.error("Error fetching categories:", error);
        });
    },
  },
  getters: {
    allCategories: (state) => state.categories,
  },
};
