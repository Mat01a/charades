<script setup lang="ts">
const value = ref(null)
const openModal = ref(false)
const dissmissible = ref(false)
const emits = defineEmits(['value', 'dissmissible'])
const props = defineProps({'text': String, 'dissmissible': Boolean, 'openModal': Boolean})
const cc = ref(false)
function submit()
{
    if (value.value)
    {
        openModal.value = false
        emits('value', value)
    }
}

function onClose()
{
    emits('dissmissible', false)
}
openModal.value = props.openModal
dissmissible.value = props.dissmissible

watch(() => [props.openModal, props.dissmissible], ([newOpenModal, newDissmissible]) => {
    openModal.value = newOpenModal;
    dissmissible.value = newDissmissible;
})



</script>

<template>
    <ClientOnly>
        <UModal :dismissible="dissmissible" v-model:open="openModal" v-on:after:leave="onClose">
            <!-- modal -->
            <template #content>
                <div class="h-32 mt-12 m-6 grid col-span-12 row-span-12 gap-4">
                    <div class="col-span-12 row-span-1 text-2xl text-center">{{ props.text }}</div>
                    <div class="col-span-12 row-span-11 h-full text-center p-4">
                        <UInput v-model="value" />
                        <UButton type="submit" v-on:click="submit" class="ml-8">Submit</UButton>
                    </div>
                </div>
            </template>
        </UModal>
    </ClientOnly>
</template>