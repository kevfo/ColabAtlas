function updateFieldInJSON(obj, fieldToUpdate, newValue) {
    // Base case: If the object is not an object or array, return it as is
    if (typeof obj !== 'object' || obj === null) {
        return obj;
    }

    // If the object is an array, iterate through its elements
    if (Array.isArray(obj)) {
        for (let i = 0; i < obj.length; i++) {
            obj[i] = updateFieldInJSON(obj[i], fieldToUpdate, newValue);
        }
    return obj;
    }

    // If the object is an object, iterate through its properties
    for (let key in obj) {
        if (obj.hasOwnProperty(key)) {
            // If the property is an object, recursively update its sub-properties
            if (typeof obj[key] === 'object' && obj[key] !== null) {
            obj[key] = updateFieldInJSON(obj[key], fieldToUpdate, newValue);
            }
            // Update the specified field if it exists
            if (key === fieldToUpdate) {
                obj[key] = newValue;
            }
        }
    }
    return obj;
}