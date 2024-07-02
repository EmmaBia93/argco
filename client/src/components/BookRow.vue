<template>
  <tr>
    <td>{{ index }}</td>
    <td>{{ book.title }}</td>
    <td>{{ `${book.author.first_name} ${book.author.last_name}` }}</td>
    <td>
      <router-link :to="'/admin/book/' + book.id">Editar</router-link>
      <button @click="handleDelete">Eliminar</button>
    </td>
  </tr>
</template>

<script>
export default {
  props: {
    book: Object,
    index: Number
  },
  methods: {
    handleDelete() {
      if (confirm(`¿Estás seguro de que quieres eliminar el ${this.book.title}?`)) {
        this.$store.dispatch('books/deleteBook', this.book.id)
        .then(() => {
            console.log('Libro eliminado correctamente');
          })
        .catch(error => {
            console.error('Error al eliminar libro:', error);
        });
      }
    }
  }
}
</script>