<template>
    <div class="main"><h1>main content</h1></div>
</template>
<script>
// import TextChatItem from '../components/TextChatItem.vue'


export default {
    name:'MainContent',
    // components:{TextChatItem,DateChatItem,ChatBox},
    mounted(){
        
    },
    data:() => ({
        textChats:[1,2,3,4,5]
    }),
    // computed:{
    //     randKey(){
    //         return Math.round(Math.random()*90)
    //     }
    // }
}
</script>
<style lang="scss" scoped>
$track-bg:#ffffff;

</style>