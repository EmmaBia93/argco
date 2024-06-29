<template>
  <div class="search-bar">
    <input
      type="text"
      v-model="query"
      placeholder="Buscar libros..."
      @input="handleInput"
    />
  </div>
</template>

<script>
export default {
  data() {
    return {
      query: "" 
    };
  },
  methods: {
    handleInput() {
      this.$emit("search", this.query);
    }
  }
};
</script>
