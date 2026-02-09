<script setup lang="ts">
// WS connection
const socket = new WebSocket("ws://127.0.0.1:8000/ws/chat/")

// Refs
const username = ref('')
const isOpened = ref(true)
const pickedColor = ref(null)
const pickedTool = ref(null)
const chatInput = ref(null)

let canvasWidth = 0
let canvasHeight = 0
const messages = []

function saveUsername()
{
    isOpened.value = false
}

function chooseColor(color)
{
    pickedColor.value = color
}


onMounted(() => {

    const canvas = document.querySelector("#canvas");
    const ctx = canvas.getContext("2d");

    canvasWidth = canvas.offsetWidth
    canvasHeight = canvas.offsetHeight
    ctx.canvas.width = canvasWidth
    ctx.canvas.height = canvasHeight

    ctx.strokeStyle = pickedColor.value;
    ctx.lineJoin = "round";
    ctx.lineCap = "round";
    ctx.lineWidth = 10;

    let isDrawing = false;
    let lastX = 0;
    let lastY = 0;
    let direction = true;
    canvas.addEventListener("mousedown", (e) => {
	isDrawing = true
	lastX = e.offsetX
	lastY = e.offsetY

    //WS connection
    socket.onopen = () => {}
})

onBeforeUnmount(() =>
{
    socket.close() 
})

canvas.addEventListener("mousemove", draw)
canvas.addEventListener("mouseup", () => {
    isDrawing = false
})

function draw(e)
{
	if (!isDrawing) return;

	ctx.strokeStyle = pickedColor.value
	ctx.beginPath()
	ctx.moveTo(lastX, lastY)
	ctx.lineTo(e.offsetX, e.offsetY)
	ctx.stroke()
	lastX = e.offsetX
	lastY = e.offsetY

}

})


function clearCanvas()
{
    const canvas = document.querySelector("#canvas")
    const ctx = canvas.getContext("2d")
	ctx.clearRect(0, 0, canvasWidth, canvasHeight)
}

function sendMessage()
{
    let currentMessage = `${username.value}: ${chatInput.value}`
    messages.push(currentMessage)
    chatInput.value = null
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
            <div class="row-start-3 row-span-10 col-span-12 bg-neutral-50 rounded-sm grid grid-cols-12">
                <div class="col-span-1 bg-neutral-200 rounded-l-sm">
                    <div class="grid grid-cols-2 gap-2 h-full grid-rows-12 p-2">
                        <ColorButton @click="() => {chooseColor('green')}" class="col-span-1 row-span-1 bg-green-500"/>
                        <ColorButton @click="() => {chooseColor('red')}" class="col-span-1 row-span-1 bg-red-500"/>
                        <ColorButton @click="() => {chooseColor('orange')}" class="col-span-1 row-span-1 bg-orange-500"/>
                        <ColorButton @click="() => {chooseColor('brown')}" class="col-span-1 row-span-1 bg-yellow-900"/>
                        <ColorButton @click="() => {chooseColor('yellow')}" class="col-span-1 row-span-1 bg-yellow-500"/>
                        <ColorButton @click="() => {chooseColor('blue')}" class="col-span-1 row-span-1 bg-blue-500"/>
                        <ColorButton @click="() => {chooseColor('purple')}" class="col-span-1 row-span-1 bg-purple-500"/>
                        <ColorButton @click="() => {chooseColor('white')}" class="col-span-1 row-span-1 bg-white"/>
                        <ColorButton @click="() => {chooseColor('gray')}" class="col-span-1 row-span-1 bg-gray-500"/>
                        <ColorButton @click="() => {chooseColor('black')}" class="col-span-1 row-span-1 bg-black"/>

                        <!-- buttons -->
                         <UButton class="col-span-2 bg-slate-300 justify-center row-span-1" v-on:click="clearCanvas" >
                            <UIcon name="i-mdi:eraser" class="bg-slate-900 scale-200"/>
                         </UButton>
                         <UButton class="col-span-2 bg-slate-300 justify-center">
                            <UIcon name="i-material-symbols:brush" class="bg-slate-900 scale-200"/>
                         </UButton>
                    </div>
                </div>
                <div class="col-span-8 bg-neutral-100">
                    <canvas class="w-full h-full rounded-sm" id="canvas" />
                </div>
                <!-- chat -->
                <div class="col-start-10 col-span-3 bg-neutral-200 rounded-r-sm p-2 text-slate-900">
                    <div class="w-full h-113">
                        <p v-for="message in messages">
                            {{ message }}
                        </p>
                    </div>
                    <div class="w-full h-10 my-2 py-1 bg-neutral-300 grid grid-cols-12 grid-rows-2 overflow-hidden p-2 gap-2">
                        <input type="text" class="p-2 col-span-9 h-8" v-model="chatInput"/>
                        <UButton type="submit" class="col-span-2 m-auto cursor-pointer hover:bg-green-500 transition-all duration-500 ease-in-out text-white font-bold" @click="sendMessage">Send</UButton>
                    </div>
                </div>
            </div>
        </div>
    </div>        


</template>
