<template>
    <div>
        My First Vue App
    </div>
</template>
<script lang="ts">
    import { Component, Vue } from 'vue-property-decorator'

    @Component({
        name: "App"
    })
    export default class App extends Vue {

    }
</script>