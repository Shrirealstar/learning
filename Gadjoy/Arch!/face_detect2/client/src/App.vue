<template>
  <div id="app">
    <FacialLandmarkDetection />
  </div>
</template>

<script>
import FacialLandmarkDetection from './components/FacialLandmarkDetection.vue';

export default {
  components: {
    FacialLandmarkDetection,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
