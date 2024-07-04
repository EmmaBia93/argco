<template>
  <div v-if="book" class="book-detail">
    <!-- Primera fila -->
    <div class="row">
      <!-- Columna izquierda: Imagen -->
      <div class="column-left">
        <img :src="book.cover" :alt="book.title">
      </div>
      
      <!-- Columna derecha: Información -->
      <div class="column-right">
        <h3>{{ book.title }}</h3>
        <p>{{ `${book.author.last_name}, ${book.author.first_name}` }}</p>
        <ul>
          <li><strong>ISBN:</strong> {{ book.isbn }}</li>
          <li><strong>Categoría:</strong> {{ book.category.name }}</li>
          <li><strong>Fecha de publicación:</strong> {{ formatDate(book.publication_date) }}</li>
        </ul>
      </div>
    </div>

    <!-- Segunda fila -->
    <div class="row">
      <!-- Columna izquierda: Descripción -->
      <div class="column-left">
        <p>Descripción</p>
      </div>
      
      <!-- Columna derecha: Sinopsis -->
      <div class="column-right">
        <p>{{ book.synopsis }}</p>
      </div>
    </div>
  </div>

  <div v-else>
    <p>Cargando...</p>
  </div>
</template>

<style>
.book-detail {
  padding: 16px;
}

.row {
  display: flex;
  margin-bottom: 16px;
}

.column-left {
  flex: 1;
  padding-right: 16px;
}

.column-right {
  flex: 2;
}

.column-left p,
.column-right p {
  margin: 0;
}

.column-left img {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
}

ul {
  list-style-type: none;
  padding: 0;
}

ul li {
  margin-bottom: 8px;
}
</style>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  props: ['id'],
  computed: {
    ...mapState('books', { book: state => state.book })
  },
  methods: {
    ...mapActions('books', ['fetchBook']),
    formatDate(dateString) {
      const options = { day: '2-digit', month: '2-digit', year: 'numeric' };
      const date = new Date(dateString);
      return date.toLocaleDateString('es-ES', options);
    }
  },
  created() {
    this.fetchBook(this.id);
  }
}
</script>