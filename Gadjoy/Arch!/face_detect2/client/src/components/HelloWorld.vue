<template>
  <div class="hello">
    <h2>{{ msg }}</h2>
    <p>For more details, visit the <a href="https://vuejs.org" target="_blank" rel="noopener noreferrer">Vue.js documentation</a>.</p>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data() {
    return {
      msg: 'Hello World!',
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.hello {
  margin-top: 20px;
  padding: 20px;
  border: 1px solid #ccc;
  background-color: #f9f9f9;
}
</style>
