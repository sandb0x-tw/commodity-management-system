<template>
    <div class="">
        <label>群組：</label>
        <span class="pr-2" v-for="tag in tags">
            <a :href=`/category/?category=${tag}`>{{ tag }}</a>, 
        </span>
    </div>
    <div v-if="items.length">
        <br/>
        <hr/>
        <br/>
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
    </div>
	 <div class="text-center">
        <a href="#" v-if="page != 0" @click="prev" class="px-3">前一頁</a>
        <a href="#" v-if="items.length == 30" @click="next" class="px-3">後一頁</a>
    </div>
</template>

<script>
    const { createApp } = Vue;

    createApp({
        data() {
            return {
                tags: [[ tags ]],
                items: [[ items ]],
                page: 0,
            }
        },
        mounted() {
            const params = new URLSearchParams(window.location.search);
            if (params.has("page")) {
              this.page = parseInt(params.get("page"), 10) || 0;
            } else {
              params.set("page", 0);
              const newUrl = `${window.location.pathname}?${params.toString()}`;
              window.history.replaceState(null, "", newUrl);
            }
        },
        methods: {
            prev() {
                this.page--;
                this.updatePageParam();
            },
            next() {
                this.page++;
                console.log(this.page)
                this.updatePageParam();
            },
            updatePageParam() {
                const params = new URLSearchParams(window.location.search);
                params.set("page", this.page);

                window.location.search = params.toString();
            }
        },
        template: document.querySelector('template').innerHTML,
    }).mount('#app')
</script>

