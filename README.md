# optimization-task
this is a solution to solve the below problem, the coe is written in python 2.7
Problem Statement:
The following are the available machines along with their respective capacities.

Large – 10 units
XLarge – 20 units 
2XLarge – 40 units
4XLarge – 80 units
8XLarge – 160 units
10XLarge – 320 units
These machines are located all over the world and depending on which part of the world they are located in, they have associated costs based on the number of hours they are utilised. Below are the per hour costs

 	New York	India	China
Large	$ 120	$ 140	$ 110
XLarge	$ 230	 	$ 200
2XLarge	$ 450	$ 413	 
4XLarge	$ 774	$ 890	$670
8XLarge	$1400	$ 1300	$ 1180
10XLarge	$ 2820	$ 2970	 
 
Write an optimized resource allocator program that can be used for cost planning. The program takes the below 2 inputs:

Hours: No of hours the machine is required to run

Capacity: No of units are required (Will always be multiple of 10)

Based on these inputs, the program should optimally allocate the resources such that the cost of the capacity required is minimum. Calculate this for every region and show them  as the below example.

10801-1
Sample Input: 

Capacity of 1150 units for 1 Hour

 

Expected Output:

{

  “Output”: [

    {

      “region”: “New York”,

      “total_cost”: “$10150”,

      “machines”: [

        (8XLarge, 7),

        (XLarge, 1),

        (Large, 1)

      ]

    },

    {

      “region”: “India”,

      “total_cost”: “$9520”,

      “machines”: [

        (8XLarge, 7),

        (Large, 3)

      ] 

    },

    {

      “region”: “China”,

      “total_cost”: “$8580”,

      “machines”: [

        (8XLarge, 7),

        (XLarge, 1),

        (Large, 1)

      ] 

    },

  ]

}

