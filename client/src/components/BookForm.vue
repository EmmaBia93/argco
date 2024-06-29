<template>
  <form @submit.prevent="submitForm">
    <!-- ISBN -->
    <div>
      <label for="isbn">ISBN</label>
      <input v-model="book.isbn" type="text" id="isbn" name="isbn" required />
    </div>

    <!-- Título -->
    <div>
      <label for="title">Título</label>
      <input v-model="book.title" type="text" id="title" name="title" required />
    </div>

    <!-- Portada -->
    <div>
      <label for="cover">Portada</label>
      <input v-model="book.cover" type="text" id="cover" name="cover" required />
    </div>

    <!-- Sinopsis -->
    <div>
      <label for="synopsis">Sinopsis</label>
      <textarea v-model="book.synopsis" name="synopsis" id="synopsis" cols="30" rows="10" required></textarea>
    </div>

    <!-- Fecha de Publicación -->
    <div>
      <label for="publication_date">Fecha de Publicación</label>
      <input v-model="book.publication_date" type="date" id="publication_date" name="publication_date" required />
    </div>

    <!-- Nombre del Autor -->
    <div>
      <label for="author_first_name">Nombre del Autor</label>
      <input v-model="book.author_first_name" type="text" id="author_first_name" name="author_first_name" required />
    </div>

    <!-- Apellido del Autor -->
    <div>
      <label for="author_last_name">Apellido del Autor</label>
      <input v-model="book.author_last_name" type="text" id="author_last_name" name="author_last_name" required />
    </div>

    <!-- Categoría -->
    <div>
      <label for="category_id">Categoría</label>
      <select v-model="book.category_id" id="category_id" required>
        <option v-for="category in categories" :key="category.id" :value="category.id">
          {{ category.name }}
        </option>
      </select>
    </div>

    <button type="submit">Guardar</button>
  </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  props: ['id'],
  data() {
    return {
      book: {
        isbn: '',
        title: '',
        cover: '',
        synopsis: '',
        publication_date: '',
        author_first_name: '',
        author_last_name: '',
        category_id: 0
      },
    }
  },
  computed: {
    ...mapGetters('categories', ['allCategories']),
    ...mapGetters('books', ['currentBook']),
    categories() {
      return this.allCategories;
    }
  },
  watch: {
    currentBook: {
      handler(newBook) {
        if (newBook) {
          this.book = {
            isbn: newBook.isbn,
            title: newBook.title,
            cover: newBook.cover,
            synopsis: newBook.synopsis,
            publication_date: new Date(newBook.publication_date).toISOString().substr(0, 10),
            author_first_name: newBook.author.first_name,
            author_last_name: newBook.author.last_name,
            category_id: newBook.category.id
          };
        } else {
          this.resetForm();
        }
      },
      immediate: true
    }
  },
  methods: {
    ...mapActions('categories', ['fetchCategories']),
    ...mapActions('books', ['fetchBook', 'createBook', 'updateBook']),
    getBook() {
      if (this.id && this.id !== 'create') {
        this.fetchBook(this.id);
      }
    },
    submitForm() {
      if (this.id !== 'create') {
        this.updateBook({ id: this.id, book: this.book });
      } else {
        this.createBook(this.book);
      }
    },
    resetForm() {
      this.book = {
        isbn: '',
        title: '',
        cover: '',
        synopsis: '',
        publication_date: '',
        author_first_name: '',
        author_last_name: '',
        category_id: 0
      };
    },
  },
  created() {
    this.fetchCategories();
    this.getBook();
  }
}
</script>