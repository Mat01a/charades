<script setup lang="ts">
const username = ref('')
const isOpened = ref(true)
function saveUsername()
{
    isOpened.value = false
}
</script>

<template>
    <div class="grid grid-cols-12 grid-rows-6 max-w-7xl w-full h-screen m-auto">
        <div class="row-span-1 col-span-12 text-center font-bold text-4xl p-8">Puns game: {{ username }}</div>
        <div class="row-start-2 row-span-4 col-start-2 col-span-10 bg-slate-800 rounded-xl shadow-2xl grid grid-cols-12 grid-rows-12 p-4">
            <ClientOnly>
                <UModal :dismissible="true" v-model:open="isOpened">
                    <!-- modal -->
                    <template #content>
                        <div class="h-32 mt-12 m-6 grid col-span-12 row-span-12 gap-4">
                            <div class="col-span-12 row-span-1 text-2xl text-center">Input name:</div>
                            <div class="col-span-12 row-span-11 h-full text-center p-4">
                                <UInput v-model="username" />
                                <UButton type="submit" v-on:click="saveUsername" class="ml-8">Submit</UButton>
                            </div>
                        </div>
                    </template>
                </UModal>
            </ClientOnly>
        </div>
    </div>        


</template>