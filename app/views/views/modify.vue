<template>
    <form action="/api/products/[[ product_id ]]" method="POST" enctype="multipart/form-data">
        <label>名稱：</label><input name="name" v-model="name" class="border w-1/2 border-gray-400" /><br/><br/>
        <label>標籤（用空白隔開）：</label><input name="tags" v-model="tags" class="border w-1/2 border-gray-400" /><br/><br/>
        <label class="inline-flex items-center cursor-pointer">
            <span class="text-sm font-medium text-gray-900 dark:text-gray-300">是否公開：</span>
            <input name="visible" type="checkbox" v-model="visible" class="sr-only peer">
            <div class="ms-3 relative w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 dark:peer-focus:ring-blue-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-blue-600"></div>
        </label><br/><br/>
        <hr/>
        <br/>
        <p>圖片：</p>
        <div class="grid grid-cols-12">
            <input name="removedImageInfo" class="hidden" v-model="removedImageInfo" />
            <div class="m-4 col-span-12 sm:col-span:6 md:col-span-4 lg:col-span-3 aspect-square" v-for="(input, index) in existingImages" :key="index">
                <a href="#" @click="delImage(index)">移除此圖片</a>
                <div v-if="input.url">
                    <img :src="input.url" alt="圖片預覽" class="w-full h-full object-cover">
                </div>
            </div>
        </div>
        <br/>
        <hr/>
        <br/>
        <label>上傳新圖片：</label><input name="newImages" type="file" multiple @change="handleFilesChange" />
        <div class="grid grid-cols-12">
            <div class="m-4 col-span-12 sm:col-span:6 md:col-span-4 lg:col-span-3" v-for="(input, index) in inputs" :key="index">
              <div v-if="input.url">
                <img :src="input.url" alt="圖片預覽" class="w-full h-full object-cover">
              </div>
            </div>
        </div>
        <br/>
        <hr/>
        <br/>
        <textarea rows="10" name="description" v-model="description" class="w-full border border-gray-400"></textarea>
        <button class="float-right border border-gray-400 p-2 hover:text-gray-400" type="submit">Submit</button>
    </form>
</template>

<script>
    const { createApp } = Vue;

    createApp({
        data() {
            return {
                inputs: [],
                existingImages: [[ existingImages ]],
                removedImages: [],
                name: [[ name ]],
                tags: [[ tags ]],
                description: [[ description ]],
                visible: [[ visible  ]],
            }
        },
        methods: {
            delImage(index) {
                this.removedImages.push(this.existingImages[index].id);
                this.existingImages.splice(index, 1);
            },
            handleFilesChange(event, index) {
                this.inputs = Array.from(event.target.files)
                this.inputs.forEach(f => {
                    const url = URL.createObjectURL(f);
                    f.url = url;
                })
                console.log(this.inputs)
            }
        },
        computed: {
            removedImageInfo: {
                get() {
                    return this.removedImages.join(',')
                }
            }
        },
        template: document.querySelector('template').innerHTML,
    }).mount('#app')
</script>

