<template>
    <p class="text-4xl">{{ product_data.name }}</p>
    <div>
        群組：<span v-for="tag in product_data.tags" class="px-1"><a :href=`/category/?${tag}`>{{ tag }}</a><span>
    </div>

    <div v-if="product_data.hasOwnProperty('images') && product_data.images.length > 1" id="custom-controls-gallery" class="relative w-full" data-carousel="static">
		<div class="relative h-56 overflow-hidden rounded-lg md:h-96">
			<div class="hidden duration-700 ease-in-out" data-carousel-item v-for="image in product_data.images">
                <img :src="image" class="absolute block max-w-full h-auto -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2" alt="圖片預覽">
			</div>
		</div>
		<div class="flex justify-center items-center pt-4">
			<button type="button" class="flex justify-center items-center me-4 h-full cursor-pointer group focus:outline-none" data-carousel-prev>
				<span class="text-gray-400 hover:text-gray-900 dark:hover:text-white group-focus:text-gray-900 dark:group-focus:text-white">
					<svg class="rtl:rotate-180 w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 10">
						<path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 5H1m0 0 4 4M1 5l4-4"/>
					</svg>
					<span class="sr-only">Previous</span>
				</span>
			</button>
			<button type="button" class="flex justify-center items-center h-full cursor-pointer group focus:outline-none" data-carousel-next>
				<span class="text-gray-400 hover:text-gray-900 dark:hover:text-white group-focus:text-gray-900 dark:group-focus:text-white">
					<svg class="rtl:rotate-180 w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 10">
						<path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 5h12m0 0L9 1m4 4L9 9"/>
					</svg>
					<span class="sr-only">Next</span>
				</span>
			</button>
		</div>
	</div>
    <div class="container">
        <img v-if="product_data.hasOwnProperty('images') && product_data.images.length == 1" :src="product_data.images[0]" class="mx-auto w-2/3 sm:w-1/3" alt="圖片預覽">
    </div>
    <br/>
    <hr/>
    <br/>
    <div class="px-10 description" v-html="description"></div>

</template>

<script>
    const { createApp  } = Vue;

    createApp({
        data() {
            return {
                product_data: [[ product_data ]],
                description: '',
            }
        },
        mounted() {
            console.log(this.product_data)
            this.description = marked.parse(this.product_data['description']);
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
