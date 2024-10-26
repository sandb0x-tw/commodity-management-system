<template>
    <div class="px-10 description" v-html="description"></div>
</template>

<script>
    const { createApp  } = Vue;

    createApp({
        data() {
            return {
                description: [[ description ]],
            }
        },
        mounted() {
            console.log(this.product_data)
            this.description = marked.parse(this.description);
        },
        template: document.querySelector('template').innerHTML,
    }).mount('#app')
</script>

<style>

.description {
  font-size: 1rem;
}

.description h1 {
  font-size: 3.5rem;
}

.description h2 {
  font-size: 2.7rem;
}

.description h3 {
  font-size: 2.2rem;
}

.description h4 {
  font-size: 1.9rem;
}

.description h5 {
  font-size: 1.7rem;
}

.description h6 {
  font-size: 1.5rem;
}

.description img {
  margin-top: 1em;
  margin-bottom: 1em;
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 100%;
  text-align: center;
}

@media (min-width: 1024px) {
  .description img {
    width: 50%;
  }
}

.description p {
  padding-top: 0.5em;
  padding-bottom: 0.5em;
}
.description ul {
  list-style-type: disc;
  padding-left: 20px;
}
.description ol {
  list-style-type: decimal;
  padding-left: 40px;
}

</style>
