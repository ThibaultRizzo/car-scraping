const getColor = (nbMax = 1) => {
    let index = 0;
    return () => {
        // Sends back the color and increment
        if (index < nbMax) return `hsla(${index++ * (255 / nbMax)}, 100%, 50%, 1)`;
    }
}

export { getColor }