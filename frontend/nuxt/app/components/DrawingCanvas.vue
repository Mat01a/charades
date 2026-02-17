<script setup lang="ts">

const emits = defineEmits<{
    (e: 'sendSocket', value: JSON): void
}>()
defineExpose({clearCanvas, draw, reciveDrawing})


const canvas = ref<HTMLCanvasElement | null>(null)
let ctx = null
let canvasWidth = 0
let canvasHeight = 0

// Painting
const pickedColor = ref('black')
let isDrawing = false;
let lastX = 0;
let lastY = 0;
onMounted(() => {

    ctx = canvas.value.getContext("2d");

    canvasWidth = canvas.value.offsetWidth
    canvasHeight = canvas.value.offsetHeight
    ctx.canvas.width = canvasWidth
    ctx.canvas.height = canvasHeight

    ctx.strokeStyle = pickedColor.value;
    ctx.lineJoin = "round";
    ctx.lineCap = "round";
    ctx.lineWidth = 10;

    canvas.value.addEventListener("mousedown", (e) => {
        isDrawing = true
        lastX = e.offsetX
        lastY = e.offsetY
    })
    canvas.value.addEventListener("mousemove", draw)
    canvas.value.addEventListener("mouseup", () => {
        isDrawing = false
    })
})

function drawLine(ctx, startX, startY, endX, endY, color)
{
    ctx.strokeStyle = color
    ctx.beginPath()
    ctx.moveTo(startX, startY)
    ctx.lineTo(endX, endY)
    ctx.stroke()
}


function draw(e)
{
    if (!isDrawing)
        return

    emits('sendSocket', {"type": "draw", "color": pickedColor.value, "last_x": lastX, "last_y": lastY, "offset_x": e.offsetX, "offset_y": e.offsetY})
    drawLine(ctx, lastX, lastY, e.offsetX, e.offsetY, pickedColor.value)

    lastX = e.offsetX
    lastY = e.offsetY
}
function reciveDrawing(e)
{
    isDrawing = true
    lastX = e.last_x
    lastY = e.last_y
    drawLine(ctx, lastX, lastY, e.offset_x, e.offset_y, e.color)
    isDrawing = false
}

function clearCanvas()
{
    const canvas = document.querySelector("#canvas")
    const ctx = canvas.getContext("2d")
	ctx.clearRect(0, 0, canvasWidth, canvasHeight)
}


</script>

<template>
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
    <div class="col-span-8 bg-white">
        <canvas class="w-full h-full rounded-sm" id="canvas" ref="canvas"/>
    </div>
</template>