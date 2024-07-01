import bookService from "../services/bookService";

export default {
  namespaced: true,
  state: {
    books: [],
    book: null,
  },
  mutations: {
    SET_BOOKS(state, books) {
      state.books = books;
    },
    SET_BOOK(state, book) {
      state.book = book;
    },
  },
  actions: {
    fetchBooks({ commit }) {
      bookService
        .getBooks()
        .then((response) => {
          commit("SET_BOOKS", response.data);
        })
        .catch((error) => console.error("Error fetching books:", error));
    },
    fetchBook({ commit }, id) {
      bookService
        .getBook(id)
        .then((response) => {
          commit("SET_BOOK", response.data);
        })
        .catch((error) => console.error("Error fetching book:", error));
    },
    createBook({ dispatch }, book) {
      bookService
        .createBook(book)
        .then(() => {
          dispatch("fetchBooks");
        })
        .catch((error) => console.error("Error creating book:", error));
    },
    updateBook({ dispatch }, { id, book }) {
      bookService
        .updateBook(id, book)
        .then(() => {
          dispatch("fetchBooks");
        })
        .catch((error) => console.error("Error updating book:", error));
    },
    deleteBook({ dispatch }, id) {
      bookService
        .deleteBook(id)
        .then(() => {
          dispatch("fetchBooks");
        })
        .catch((error) => console.error("Error deleting book:", error));
    },
  },
  getters: {
    allBooks: (state) => state.books,
    currentBook: (state) => state.book,
  },
};
