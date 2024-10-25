<template>
    <form action="/api/products/{{ product_id  }}" method="POST" enctype="multipart/form-data">
        <label>商品名稱：</label><input name="name" v-model="name" class="border w-1/2 border-gray-400" /><br/><br/>
        <label>商品標籤（用空白隔開）：</label><input name="tags" v-model="tags" class="border w-1/2 border-gray-400" /><br/><br/>
        <hr/>
        <br/>
        <p>商品圖片：</p>
        <div class="grid grid-cols-12">
            <input name="removedImageInfo" class="hidden" v-model="removedImageInfo" />
            <div class="m-4 col-span-12 sm:col-span:6 md:col-span-4 lg:col-span-3" v-for="(input, index) in existingImages" :key="index">
              <a href="#" @click="delImage(index)">移除此圖片</a>
              <div v-if="input.url">
                <img :src="input.url" alt="圖片預覽">
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
                <img :src="input.url" alt="圖片預覽">
              </div>
            </div>
        </div>
        <br/>
        <hr/>
        <br/>
        <textarea name="description" v-model="description" class="w-full border border-gray-400"></textarea>
        <button class="border border-gray-400 p-2 hover:text-gray-400" type="submit">Submit</button>
    </form>
</template>

<script>
    const { createApp, ref } = Vue;

    createApp({
        data() {
            return {
                inputs: [],
                existingImages: {{ existingImages }},
                removedImages: [],
                name: "{{ name }}",
                tags: "{{ tags }}",
                description: "{{ description }}",
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

