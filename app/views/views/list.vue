<template>
    <div class="grid grid-cols-12">
        <div class="m-4 col-span-12 sm:col-span:6 md:col-span-4 lg:col-span-3 text-center " v-for="item in items">
            <a :href=`/product/${item.id}`>
                <div class="aspect-square">
                    <p class="text-xl">{{ item.name }}</p>
                    <img :src="item.image" alt="圖片預覽" class="w-full h-full object-cover">
                </div>
            </a>
            <span v-for="tag in item.tags" class="px-1">
                <a :href=`/category/?${tag}`>{{ tag }}</a>
            <span>
        </div>
    </div>
</template>

<script>
    const { createApp } = Vue;

    createApp({
        data() {
            return {
                items: [[ items ]],
            }
        },
        template: document.querySelector('template').innerHTML,
    }).mount('#app')
</script>

