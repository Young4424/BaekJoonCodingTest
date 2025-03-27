#include <queue>
#include <cstdio>
using namespace std;

int main() {
    int N,K,i,j,temp,flag;
    queue <int> q;
    scanf("%d %d",&N, &K);

    for(i = 1; i<= N; i++){
        q.push(i);
    }

    printf("<");
    while(q.size()){
        if (q.size() == 1){
            printf("%d>\n",q.front());
            q.pop();
            break;
        }
        for(j = 0; j < K-1; j++){
            q.push(q.front());
            q.pop();
        }
        printf("%d, ",q.front());
        q.pop();

    }
    return 0;

}