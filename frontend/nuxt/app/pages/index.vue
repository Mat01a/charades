<script setup lang="ts">
import DrawingCanvas from '~/components/DrawingCanvas.vue'
import type { ChatMessage } from '~/types/chat-message'
import type { DrawingData } from '~/types/drawing-data'

// Refs
const username = ref('')
const isOpened = ref(true)
const pickedTool = ref(null)
const chatInput = ref(null)
const roomName = ref(null)
const canvas = ref(null)
const messages = ref([])
// WS connection
let socket


function saveUsername()
{
    isOpened.value = false
}

function chooseColor(color)
{
    pickedColor.value = color
}

onUpdated(() => {
    // HACK: not sending color through socket
    // HACK: not clear canvas on eraser button through sockets
})


onBeforeUnmount(() => {
 // Close connection on closing web
 if (socket)
     socket.close()
})

function sendMessage(data)
{
    // FIXME: requires proper error catching
    try
    {
        socket.send(JSON.stringify({"type": "message", "username": username.value, "message": data.message}))
        
    }
    catch(e)
    {
        console.log(JSON.stringify(e))
    }
    chatInput.value = null
}

function connect()
{
    let url = "ws://127.0.0.1:8000/ws/chat/" + roomName.value
    socket = new WebSocket(url)
    socket.onopen = () => {
        canvas.value.clearCanvas()
        messages.value = []
    }

    socket.onmessage = (message) => {
    let parsedJson = JSON.parse(message.data)
    if (parsedJson.type == 'message')
    {
        let currentMessage = parsedJson.user + ":" + parsedJson.message
        messages.value.push(currentMessage)
    }
    else if (parsedJson.type == 'recive_draw')
    {
        if (parsedJson.username != username.value)
        {
            canvas.value.reciveDrawing(parsedJson)
        }
    }
}

}

function sendDrawing(data: DrawingData)
{
    const new_data = JSON.stringify({"type": data.type, "color": data.color, "username": username.value, "last_x": data.last_x, "last_y": data.last_y, "offset_x": data.offset_x, "offset_y": data.offset_y})
    socket.send(new_data)
}


</script>

<template>
    <div class="grid grid-cols-12 grid-rows-6 max-w-7xl w-full h-screen m-auto">
        <div class="row-span-1 col-span-12 text-center font-bold text-4xl p-8">Puns game: {{ username }}</div>
        <div class="row-start-2 row-span-4 col-start-2 col-span-10 bg-slate-800 rounded-xl shadow-2xl grid grid-cols-12 grid-rows-12 p-4">
            <div class="row-span-2 col-span-12 grid grid-rows-3">
                <div class="px-1 row-span-1 text-lg font-bold">
                    Input room name:
                </div>
                <div class="row-span-1">
                    <UInput placeholder="room name" v-model="roomName"/>
                    <UButton class="mx-2" @click="connect">Connect</UButton>
                </div>
            </div>
            <ClientOnly>
                <UModal :dismissible="false" v-model:open="isOpened">
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
            <div class="row-start-3 row-span-10 col-span-12 bg-neutral-50 rounded-sm grid grid-cols-12">
                <DrawingCanvas @send-socket="sendDrawing" ref="canvas"/>
                <Chat @send-message="sendMessage" :messages="messages"/>
            </div>
        </div>
    </div>        


</template>
