<template>
    <div class="">
        <label>群組：</label>
        <span class="pr-2" v-for="tag in tags">
            <a :href=`/category/?category=${tag}`>{{ tag }}</a>
        </span>
    </div>
    <div v-if="items.length">
        <br/>
        <hr/>
        <br/>
        <div class="grid grid-cols-12">
            <div class="m-4 col-span-12 sm:col-span:6 md:col-span-4 lg:col-span-3 text-center" v-for="item in items">
                <a :href=`/product/${item.id}`>
                    <p class="text-xl">{{ item.name }}</p>
                    <img :src="item.image" alt="圖片預覽">
                </a>
                <span v-for="tag in item.tags" class="px-1">
                    <a :href=`/category/?category=${tag}`>{{ tag }}</a>
                <span>
            </div>
        </div>
    </div>
</template>

<script>
    const { createApp } = Vue;

    createApp({
        data() {
            return {
                tags: [[ tags ]],
                items: [[ items ]],
            }
        },
        template: document.querySelector('template').innerHTML,
    }).mount('#app')
</script>
