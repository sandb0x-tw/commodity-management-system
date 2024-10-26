<template>
    <div v-if="!isLogged">
		  <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto mt-30 sm:mt-40 lg:py-0">
			  <div class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
				  <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
					  <form class="space-y-4 md:space-y-6" action="/api/login" method="POST">
						  <div>
							  <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>
							  <input type="password" name="password" id="password" placeholder="••••••••" class="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
						  </div>
						  <button type="submit" class="w-full border text-gray-400 bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">Sign in</button>
					  </form>
				  </div>
			  </div>
		  </div>
    </div>
    <div v-if="isLogged">
        <form action="/api/modify_website" method="POST">
            <label>網站標題：</label><input name="title" v-model="title" class="border w-1/2 border-gray-400" /><br/><br/>
            <label>網站頁腳：</label><input name="footer" v-model="footer" class="border w-1/2 border-gray-400" /><br/><br/>
            <p>關於我們敘述：</p>
            <textarea rows="10" name="description" v-model="description" class="w-full border border-gray-400"></textarea>
             <button class="float-right border border-gray-400 p-2 hover:text-gray-400" type="submit">修改</button>
            <div sytle="clear: both"></div>
        </form>
        <br/>
        <br/>
        <hr/>
        <br/>
        <form action="/api/passwd" method="POST">
            <label>新密碼：</label><input name="password" class="border w-1/2 border-gray-400" />
             <button class="float-right border border-gray-400 p-2 hover:text-gray-400" type="submit">修改</button>
            <div sytle="clear: both"></div>
        </form>
        <br/>
        <br/>
        <hr/>
        <br/>
        <a href="/api/products" class="border border-gray-400 p-2 hover:text-gray-400">新增</a>
        <br/>
        <br/>
		列表：
        <br/>
        <div v-for="item in productList">
            <a :href=`/modify/${item.id}`>
                {{ item.name  }}: 
				<span v-for="tag in item.tags" class="px-1">{{ tag }}, <span>
            </a>
			<hr/>
        </div>
    </div>
</template>

<script>
    const { createApp } = Vue;

    createApp({
        data() {
            return {
                isLogged: [[ isLogged ]],
                productList: [[ productList ]],
                title: [[ title ]],
                footer: [[ footer ]],
                description: [[ description ]],
            }
        },
        template: document.querySelector('template').innerHTML,
    }).mount('#app')
</script>

