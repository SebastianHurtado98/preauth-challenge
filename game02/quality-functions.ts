function commonQualityDecrease(sellIn: number, quality: number) {
    if (sellIn == 0) {
        return 2
    } else {
        return 1
    }
}

function conjuredItemsQualityDecrease(sellIn: number, quality: number) {
    return commonQualityDecrease(sellIn, quality) * 2
}

function agedBridgedQualityDecrease(sellIn: number, quality: number) {
    return -1
}

function sulfurasQualityDecrease(sellIn: number, quality: number) {
    return 0
}

function backstagePassesQualityDecrease(sellIn: number, quality: number) {
    if (sellIn == 0) {
        return quality
    } else if (sellIn <= 5) {
        return -3
    } else if (sellIn <= 10) {
        return -2
    } else {
        return 0
    }
}

export {
    commonQualityDecrease,
    conjuredItemsQualityDecrease,
    agedBridgedQualityDecrease,
    sulfurasQualityDecrease,
    backstagePassesQualityDecrease 
}