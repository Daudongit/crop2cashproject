<template>
    <div>
        <!-- <header class="header">Hello from default</header>
        <router-link to="/login">Login</router-link> -->
        <slot/>
    </div>
</template>
<script>
export default {
    name:'DefaultLayout'
}
</script>
<style scoped>
.header{
    width: 100%;
    height: 35px;
    background-color: #350d36;
    color:white;
    font-size: 20px;
}
</style>