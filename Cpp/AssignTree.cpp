#include <iostream>
using namespace std;

struct TreeNode {
    int data;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int val) : data(val), left(nullptr), right(nullptr) {}
};

TreeNode* sortedArrayToBST(int arr[], int n) {
    if (n == 0) return nullptr;
    int mid = n / 2;
    TreeNode* root = new TreeNode(arr[mid]);
    root->left = sortedArrayToBST(arr, mid);
    root->right = sortedArrayToBST(arr + mid + 1, n - mid - 1);
    return root;
}

void preorder(TreeNode* root) {
    if (!root) return;
    cout << root->data << " ";
    preorder(root->left);
    preorder(root->right);
}

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7};
    int n = sizeof(arr) / sizeof(arr[0]);
    TreeNode* root = sortedArrayToBST(arr, n);
    cout << "Preorder traversal of the constructed BST: ";
    preorder(root);
    cout << endl;
    return 0;
}