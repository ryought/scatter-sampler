console.log('script')

function where (array) {
    var indices = []
    for (var i = 0; i < array.length; i++) {
        if (array[i] > 0) {
            indices.push(i)
        }
    }
    return indices
}

function slice (array) {
    var subarray = []
    return subarray
}

/*
    imagedata -> imagedataの関数群
     */
function erode(ctx, data) {
    var w = data.width
    var h = data.height
    var d = data.data
    var out = ctx.createImageData(width, height)
    var dx = [0, 1, 0, -1];
    for (var x = 1; x < w-1; x += 1) {
        for (var y = 1; y < h-1; y += 1) {
            var id = (x + y * w) * 4;
            var flag = d[(x + (y-1) * w) * 4 + 3] > 0
                && d[(x + (y+1) * w) * 4 + 3] > 0
                && d[((x-1) + y * w) * 4 + 3] > 0
                && d[((x+1) + y * w) * 4 + 3] > 0;
            if (flag) {
                out.data[id + 0] = d[id + 0]
                out.data[id + 1] = d[id + 1]
                out.data[id + 2] = d[id + 2]
                out.data[id + 3] = d[id + 3]
            } else {
                out.data[id + 0] = 0
                out.data[id + 1] = 0
                out.data[id + 2] = 0
                out.data[id + 3] = 0
            }
        }
    }
    return out
}
// d1 - d2
function diff(ctx, d1, d2) {
    var w = d1.width, h = d1.height
    var out = ctx.createImageData(width, height)
    for (var i = 0; i < w * h * 4; i += 4) {
        if (d1.data[i + 3] > 0) {
            if (d2.data[i + 3] > 0) {
                out.data[i] = 0
            } else {
                out.data[i] = d1.data[i]
                out.data[i+3] = d1.data[i+3]
            }
        }
    }
    return out
}

function apply_pixel_wise(ctx, data, callback) {
    /*
    callback(x, y, [r, g, b, a])が呼ばれる
     */
    var w = data.width, h = data.height
    var out = ctx.createImageData(width, height)
    for (var i = 0; i < w * h * 4; i += 4) {
        if (d1.data[i + 3] > 0) {
            if (d2.data[i + 3] > 0) {
                out.data[i] = 0
            } else {
                out.data[i] = d1.data[i]
                out.data[i+3] = d1.data[i+3]
            }
        }
    }
    return out
}
