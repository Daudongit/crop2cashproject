<template>
    <div>
        <h1>Welcome Home</h1>
        <router-link to="/login">Login</router-link>
    </div>
</template>
<script>

export default {
    name:'Home',
    created(){
        // this.$emit('update:layout',DefaultLayout)
    }
}
</script>