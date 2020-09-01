<template>
  <card :title="$t('home')">
    {{ $t('you_are_logged_in') }}
    <p>
      Continue Profile setup
    <router-link :to="{ name: 'profileSetup' }">
      {{ $t('ProfileSetup') }}
    </router-link>
  </p>
  </card>

</template>

<script>
export default {
  middleware: 'auth',

  metaInfo () {
    return { title: this.$t('home') }
  }
}
</script>
