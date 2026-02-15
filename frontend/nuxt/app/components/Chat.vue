<script setup lang="ts">
import type { ChatMessage } from '~/types/chat-message';

const chatInput = ref()
const emits = defineEmits<{
    (e: 'sendMessage', value: ChatMessage): void
}>()
const props = defineProps<{
    messages: { type: Array<String> }
}>()
const messages = ref()

function sendMessage()
{
    // FIXME: requires proper error catching
    try
    {
        console.log(chatInput.value)
        emits('sendMessage', {"type": "message", "message": chatInput.value})
        
    }
    catch(e)
    {
        console.log(JSON.stringify(e))
    }
    chatInput.value = null
}
</script>

<template>
    <div class="col-start-10 col-span-3 bg-neutral-200 rounded-r-sm p-2 text-slate-900">
        <div class="w-full h-113">
            <p v-for="message in props.messages">
                {{ message }}
            </p>
        </div>
        <div class="w-full h-10 my-2 py-1 bg-neutral-300 grid grid-cols-12 grid-rows-2 overflow-hidden p-2 gap-2">
            <input type="text" class="p-2 col-span-9 h-8" v-model="chatInput"/>
            <UButton type="submit" class="col-span-2 m-auto cursor-pointer hover:bg-green-500 transition-all duration-500 ease-in-out text-white font-bold" @click="sendMessage">Send</UButton>
        </div>
    </div>
</template>