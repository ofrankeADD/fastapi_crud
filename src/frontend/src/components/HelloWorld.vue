<template>
  <div>
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'HelloWorld', data() {
    return { msg: '', };
  },
  methods: { 
    getMessage() {
      axios.get('/').then((res) => { this.msg = res.data; }).catch((error) => { console.error(error); });
    },
  },
  created() { this.getMessage(); },
};
</script>

