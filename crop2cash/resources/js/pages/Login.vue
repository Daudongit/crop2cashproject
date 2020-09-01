<template>
    <div>
        <h1>Hellow from login page</h1>
        <router-link to="/dashboard">Dashboard</router-link>
    </div>
</template>
<script>
import LoginLayout from '../layouts/LoginLayout.vue'

export default {
    name:'Login',
    // components:{DateChatItem},
    data:()=>({
        chats:[1,2,3,4,5,6,7]
    }),
    created(){
        // this.$emit('update:layout',LoginLayout)
    }
}
</script>