#include<stdio.h>
void main()
{
  int n,rem,rev=0;
  printf("enter a number= ");
  scanf("%d",&n);

  //loop used to find reverse of entered number
  int a=n;
  while(a>0)
  {
    rem= a%10;
    rev= rev*10 + rem;
    a= a/10;
  }

  //If reverse of a number is equal to the number then it is palindrome
  if(n==rev)
  {
    printf("%d is a palindrome",n);
  }
  else
  {
    printf("%d is not a palindrome",n);
  }
}
