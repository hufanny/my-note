## 排序方式
#### HeapSort

- 會有父節點跟子節點，子節點永遠要比父節點小，直到最大的數字在最上面，然後再跟底端最小的數字交換後取出，一直重複步驟即可排列完成。

#### MergeSort

- 把一串list不斷切半，直到分成個體，然後兩組互相比較，小的放左邊大的放右邊並結合，不斷合併後就會有排好的list。
## 時間複雜度
#### HeapSort

- Best：Ο(n log n)

- Worst：Ο(n log n)

- Average：Ο(n log n)

#### MergeSort

- Best：Ο(n log n)                                            

- Worst：Ο(n log n)

- Average：Ο(n log n)
## 空間複雜度
#### HeapSort

- 只有在二元樹裡進行互換的動作，所以為O(1)

#### MergeSort

- 運用到多儲存空間來進行排序，所以為O(n)
