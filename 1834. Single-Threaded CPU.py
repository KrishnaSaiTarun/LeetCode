import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks_with_index = []
        for i in range(len(tasks)):
            tasks_with_index.append([tasks[i][0], tasks[i][1], i])
        tasks_with_index = sorted(tasks_with_index, key=lambda x: x[0])
        # tasks_with_index = List[enqueueTimei, enqueueTimei, OGIndexi]
        available_tasks, ans = [], []
        heapq.heapify(available_tasks)
        # heap has (processing time , original_index)
        # min heap based on processing time first priority and index second priority 
        # heapq.heappush(available_tasks, (tasks[0][1], tasks[0][2]))
        cur_start_time = tasks_with_index[0][0]
        cur_index = 0

        while available_tasks or cur_index < len(tasks_with_index):

            # setup if there are tasks left to process but CPU in idle state 
            # This step is required becuase there is a possibility that in between
            # there is a gap after processing few tasks before next task comes in 
            if not available_tasks and cur_start_time <= tasks_with_index[cur_index][0]:
                cur_start_time = tasks_with_index[cur_index][0]
                # make sure all that start at the same time are added to the heap
            while cur_index < len(tasks_with_index) and tasks_with_index[cur_index][0] <= cur_start_time:
                task_processing_time = tasks_with_index[cur_index][1]
                task_original_index = tasks_with_index[cur_index][2]
                heapq.heappush(available_tasks, (task_processing_time, task_original_index))
                cur_index+=1 

            # if we are here that means there is something to process 
            task_process_time, original_index_of_task_to_process = heapq.heappop(available_tasks)
            ans.append(original_index_of_task_to_process)
            # update cur_start_time so that we can add eveything before this into the heap
            cur_start_time = cur_start_time + task_process_time

        return ans 
