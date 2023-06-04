from clearml.automation import TriggerScheduler

trigger=TriggerScheduler(pooling_frequency_minutes=0.1)

trigger.add_dataset_trigger(name='Retrain on Dataset',
                            schedule_task_id='afeedf1ddeb74d08b1251e0a0e073a3f',
                            schedule_queue='default',
                            trigger_project='sarcasm_detector',
                            trigger_name='sarcasm_dataset ')

#trigger.start()

trigger.start_remotely()