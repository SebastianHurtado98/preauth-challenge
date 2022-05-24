import {
    commonQualityDecrease,
    conjuredItemsQualityDecrease,
    agedBridgedQualityDecrease,
    sulfurasQualityDecrease,
    backstagePassesQualityDecrease 
} from './quality-functions';

export class Item {
    name: string;
    sellIn: number;
    quality: number;

    constructor(name, sellIn, quality) {
        this.name = name;
        this.sellIn = sellIn;
        this.quality = quality;
    }
}

export class GildedRose {
    items: Array<Item>;

    constructor(items = [] as Array<Item>) {
        this.items = items;
    }

    private isLegendary(name: string) {
        if (name === 'Sulfuras, Hand of Ragnaros') {
            return true
        } else {
            return false
        }
    }

    private get_quality_decrease_function(name: string) {
        switch (name) {
            case 'Aged Brie':
                return agedBridgedQualityDecrease
            case 'Sulfuras, Hand of Ragnaros':
                return sulfurasQualityDecrease
            case 'Backstage passes to a TAFKAL80ETC concert':
                return backstagePassesQualityDecrease
            case 'Conjured':
                return conjuredItemsQualityDecrease
            default:
                return commonQualityDecrease
        }
    }

    updateQuality() {
        var selectedFunction: Function
        var decreaseRate: number
        this.items.forEach(item => {
            if (!this.isLegendary(item.name)) {
                item.sellIn = Math.max(0, item.sellIn - 1)
                selectedFunction = this.get_quality_decrease_function(item.name)
                decreaseRate = selectedFunction(item.sellIn, item.quality)
                item.quality = Math.max(0, item.quality - decreaseRate)
                item.quality = Math.min(50, item.quality)
            }
        });
        return this.items;
    }

    printInventory() {
        this.items.forEach(item => {
            console.log("ITEM")
            console.log("Name: " + item.name)
            console.log("Q: " + item.quality)
            console.log("Sell in: " + item.sellIn)
        });
    }

}

function test() {
    let itemsToLoad: Array<Item> = [
        {
            name: 'Common item',
            sellIn: 3,
            quality: 10,
        }
    ]

    let store = new GildedRose(itemsToLoad)

    for (let i = 0; i < 25; i++) {
        console.log("Day " + i)
        store.updateQuality()
        store.printInventory()
    }
}

test();