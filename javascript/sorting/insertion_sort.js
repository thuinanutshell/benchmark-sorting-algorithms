function insertionSort(array) {
  for (let i = 1; i < array.length; i++) {
    let key = array[i];
    let j = i - 1;
    while (j >= 0 && array[j] > key) {
      array[j + 1] = array[j]
      j --;
    }
    array[j + 1] = key
  }
  return array;
}

arr = insertionSort([1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92])
console.log(arr)